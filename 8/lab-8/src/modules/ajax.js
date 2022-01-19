import Urls from "./urls.js";

export const getStudents = async () => {
    return await fetch(Urls.Students).then((response) => response.json());
}

export const getStudent = async ({id}) =>{
    return await fetch(Urls.GetStudent(id)).then((response) => response.json());
}