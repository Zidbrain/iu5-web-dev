import {StudentComponent} from "../../components/student/StudentComponent.js";
import {BackButtonComponent} from "../../components/back-button/BackButtonComponent.js";
import {MainPage} from "../main/main.js";
import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";

export class StudentPage{
    constructor(parent, id) {
        this.parent = parent;
        this.id = id;
    }

    async getData() {
        return (await ajax.get(urls.student(this.id))).data;
    }

    get page() {
        return document.getElementById('student-page');
    }

    getHtml() {
        return (
            `
                <div id="student-page">
                </div>
            `
        )
    }

    backClicked() {
        const mainPage = new MainPage(this.parent);
        mainPage.render();
    }

    async render() {
        this.parent.innerHTML = '';
        const html = this.getHtml();
        this.parent.insertAdjacentHTML('beforeend', html);

        const backButton = new BackButtonComponent(this.page);
        backButton.render(this.backClicked.bind(this));

        const data = await this.getData();
        const student = new StudentComponent(this.page);
        student.render(data);
    }
}