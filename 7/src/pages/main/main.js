import {StockCardComponent} from "../../components/student-card/StudentCardComponent.js";
import {StudentPage} from "../student/StudentPage.js";
import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";

export class MainPage{
    constructor(parent) {
        this.parent = parent;
    }

    async getData(){
        return (await ajax.get(urls.students())).data;
    }

    get page() {
        return document.getElementById('main-page')
    }

    getHTML() {
        return (
            `
            <div id="main-page" class="d-flex flex-wrap"><div/>
        `
        )
    }

    cardClicked(e){
        const id = e.target.dataset.id;

        const studpage = new StudentPage(this.parent, id);
        studpage.render();
    }

    async render(){
        this.parent.innerHTML = '';
        const html = this.getHTML();
        this.parent.insertAdjacentHTML('beforeend', html);

        const data = await this.getData();
        data.forEach((item) => {
            const stockCard = new StockCardComponent(this.page);
            stockCard.render(item, this.cardClicked.bind(this));
        })
    }
}