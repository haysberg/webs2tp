function toc4() {
    //Getting list of H1 nodes
    list_of_h1 = document.querySelectorAll("h1");

    //inserting the table node
    introduction = list_of_h1[0];
    var table = document.createElement("table");
    document.body.insertBefore(table, document.body.firstChild);

    //Setting up element IDs
    list_of_h1.forEach((element) => {
        if (element.id == '') {
            element.id = element.innerHTML;
        }

        //Inserting the child nodes
        var el = document.createElement("td");
        el.lien = element;
        var link = document.createElement("a");
        link.href = el.lien.id;
        el.innerHTML = el.lien.innerHTML;


        el.addEventListener("mouseover", () => {
            console.log("hover");
            el.lien.setAttribute("style", "background-color: yellow;");
        });

        el.addEventListener('mouseleave', () => {
            el.lien.setAttribute("style", "background-color: none;");
        });

        link.appendChild(el);
        table.appendChild(link);
    })

    table.appendChild(document.createElement("br"));

    document.querySelectorAll("h2").forEach((element) => {
        if (element.id == '') {
            element.id = element.innerHTML;
        }

        //Inserting the child nodes
        var el = document.createElement("td");
        el.lien = element;
        var link = document.createElement("a");
        link.href = el.lien.id;
        el.innerHTML = el.lien.innerHTML;


        el.addEventListener("mouseover", () => {
            console.log("hover");
            el.lien.setAttribute("style", "background-color: red;");
        });

        el.addEventListener('mouseleave', () => {
            el.lien.setAttribute("style", "background-color: none;");
        });

        link.appendChild(el);
        table.appendChild(link);
    })
}

function toc3() {
    //Getting list of H1 nodes
    list_of_h1 = document.querySelectorAll("h1");

    //inserting the table node
    introduction = list_of_h1[0];
    var table = document.createElement("table");
    document.body.insertBefore(table, document.body.firstChild);

    //Setting up element IDs
    list_of_h1.forEach((element) => {
        if (element.id == '') {
            element.id = element.innerHTML;
        }

        //Inserting the child nodes
        var el = document.createElement("td");
        el.lien = element;
        var link = document.createElement("a");
        link.href = el.lien.id;
        el.innerHTML = el.lien.innerHTML;


        el.addEventListener("mouseover", () => {
            console.log("hover");
            el.lien.setAttribute("style", "background-color: yellow;");
        });

        el.addEventListener('mouseleave', () => {
            el.lien.setAttribute("style", "background-color: none;");
        });

        link.appendChild(el);
        table.appendChild(link);
    })
}

function toc2() {
    //Getting list of H1 nodes
    list_of_h1 = document.body.getElementsByTagName("h1");

    //inserting the table node
    introduction = list_of_h1[0];
    var table = document.createElement("table");
    document.body.insertBefore(table, document.body.firstChild);

    //Setting up element IDs
    for (var i = 0; i < list_of_h1.length; i++) {
        if (list_of_h1[i].id == '') {
            list_of_h1[i].id = list_of_h1[i].innerHTML;
        }
    }

    //Inserting the child nodes
    for (var i = 0; i < list_of_h1.length; i++) {
        var link = document.createElement("a");
        link.href = "#" + list_of_h1[i].id;
        var el = document.createElement("td");
        el.innerHTML = list_of_h1[i].innerHTML;
        link.appendChild(el);
        table.appendChild(link);
    }

}

function toc() {
    //Getting list of H1 nodes
    list_of_h1 = document.body.getElementsByTagName("h1");

    //inserting the table node
    introduction = list_of_h1[0];
    var table = document.createElement("table");
    document.body.insertBefore(table, document.body.firstChild);


    //Inserting the child nodes
    for (var i = 0; i < list_of_h1.length; i++) {
        var el = document.createElement("td");
        el.innerHTML = list_of_h1[i].innerHTML;
        table.appendChild(el);
    }

}

window.onload = toc4;