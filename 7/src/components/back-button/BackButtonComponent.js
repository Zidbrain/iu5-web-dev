export class BackButtonComponent {
    constructor(parent) {
        this.parent = parent;
    }

    addListeners(listener) {
        document
            .getElementById('back-button')
            .addEventListener("click", listener);
    }

    getHtml() {
        return (
            `
            <div class="btn btn-primary" id="back-button">Назад</div>
            `
        )
    }

    render(listener) {
        const html = this.getHtml();
        this.parent.insertAdjacentHTML('beforeend', html);
        this.addListeners(listener);
    }
}