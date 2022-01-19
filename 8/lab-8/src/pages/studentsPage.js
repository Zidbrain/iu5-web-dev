import {ListGroup} from "react-bootstrap";
import {useAsync} from "react-async";
import React from "react";
import {getStudents} from "../modules/ajax.js";

function StudentsPage() {
    const {data, status} = useAsync(getStudents);

    if (status === "pending")
        return "Loading"

    return (
        <ListGroup>
            {data.map((item, index) => {
                return (
                    <a className={"list-group-item list-group-item-action w-100"} aria-current={"true"}
                       href={`/changeStudent/` + item.idstudent}
                       key={index}>
                        <div>
                            <h1 className={"fw-bold"}>{item.last_name} {item.first_name} {item.middle_name}</h1>
                            <p className={"mb-0 opacity-75"}>Средняя оценка: {item.gpa}</p>
                        </div>
                    </a>
                )
            })}
        </ListGroup>
    );
}

export default StudentsPage;