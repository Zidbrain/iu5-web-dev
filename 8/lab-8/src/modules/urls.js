export default class Urls{
    static get Base(){
        return 'http://localhost:8000/';
    }

    static get Students(){
        return this.Base + "students/";
    }

    static GetStudent(id) {
        return this.Students + id;
    }
}