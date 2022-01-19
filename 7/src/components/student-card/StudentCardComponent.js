export class StockCardComponent{
    constructor(parent){
        this.parent = parent;
    }

    getHtml(data){
        return (
            `
                <div class="card" style="width: 300px;">
                    <div class="card-body">
                        <h5 class="card-title">${data.last_name}</h5>
                        <p class="card-text">${data.last_name} ${data.first_name} ${data.middle_name}</p>
                        <p class="card-text">Среднаяя оценка: ${data.gpa}</p>
                        <button class="btn btn-primary" id="click-${data.idstudent}" data-id="${data.idstudent}">Переход к студенту</button>
                    </div>
                </div>
            `
        );
    }

    addListeners(data, listener){
        document
            .getElementById("click-" + data.idstudent)
            .addEventListener('click', listener);
    }

    render(data, listener){
        const html = this.getHtml(data);
        this.parent.insertAdjacentHTML('beforeend', html);
        this.addListeners(data, listener);
    }
}


