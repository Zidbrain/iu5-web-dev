export class StudentComponent {
    constructor(parent) {
        this.parent = parent;
    }

    getHTML(data) {
        return (
            `
                <div class="card">
                     <div class="card-body">
                        <h5 class="card-title">${data.last_name} ${data.first_name} ${data.middle_name}</h5>
                        <p class="card-text">Средняя оценка: ${data.gpa}</p>
                     </div>
                </div>
            `
        )
    }

    render(data) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
    }
}