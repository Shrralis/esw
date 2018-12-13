/**
 * Created by HP ProBook on 16.05.2018.
 */
function changeLanguage() {
    var lan_button = document.getElementById("lan_button").getAttribute("value");
    if (lan_button == "eng") {
        document.getElementById("con_inf").innerHTML = "Contact Information";
            document.getElementById("name1").innerHTML = "Full name";
            document.getElementById("adres1").innerHTML = "Your adress";
            document.getElementById("telephone1").innerHTML = "Phone number";
        document.getElementById("obj").innerHTML = "Objectives";
            document.getElementById("Objectives1").innerHTML = "Description";
        document.getElementById("exp").innerHTML = "Work Experience";
            document.getElementById("posada1").innerHTML = "Position";
            document.getElementById("company1").innerHTML = "Name company";
            document.getElementById("city1").innerHTML = "City";
            document.getElementById("datepoch").innerHTML = "Start date";
            document.getElementById("dateend").innerHTML = "End date";
            document.getElementById("obov").innerHTML = "Duties and achievements";
        document.getElementById("edu").innerHTML = "Education";
        document.getElementById("skills").innerHTML = "Skills";
        document.getElementById("lan").innerHTML = "Languages";
        document.getElementById("int").innerHTML = "Interests";
        document.getElementById("aff").innerHTML = "Affiliations";
        document.getElementById("ref").innerHTML = "References";
        document.getElementById("sub").setAttribute("value","Save resume");
        document.getElementById("op").innerHTML = "View resume";
        document.getElementById("lan_button").setAttribute("value","ua");
    }
    else {
        document.getElementById("con_inf").innerHTML = "Контактна інформація";
            document.getElementById("name1").innerHTML = "Повне ім'я";
            document.getElementById("adres1").innerHTML = "Ваша адреса";
            document.getElementById("telephone1").innerHTML = "Номер телефону";
        document.getElementById("obj").innerHTML = "Опис";
            document.getElementById("Objectives1").innerHTML = "Опис";
        document.getElementById("exp").innerHTML = "Досвід роботи";
            document.getElementById("posada1").innerHTML = "Посада";
            document.getElementById("company1").innerHTML = "Назва компаніїі";
            document.getElementById("city1").innerHTML = "Місто";
            document.getElementById("datepoch").innerHTML = "Дата початку";
            document.getElementById("dateend").innerHTML = "Дата закінчення";
            document.getElementById("obov").innerHTML = "Обов'язки та досягнення";
        document.getElementById("edu").innerHTML = "Освіта";
        document.getElementById("skills").innerHTML = "Навики та технології";
        document.getElementById("lan").innerHTML = "Знання іноземних мов";
        document.getElementById("int").innerHTML = "Інтереси/Хобі";
        document.getElementById("aff").innerHTML = "Організації";
        document.getElementById("ref").innerHTML = "Контакти";
        document.getElementById("sub").setAttribute("value","Зберегти резюме");
        document.getElementById("op").innerHTML = "Переглянути резюме";
        document.getElementById("lan_button").setAttribute("value","eng");
    }
}

function downloadInnerHtml(filename, elId) {
    var elHtml = document.getElementById(elId).innerHTML;
    var link = document.createElement('a');
    link.setAttribute('download', filename);
    link.setAttribute('href', 'data:' + 'text/doc' + ';charset=utf-8,' + encodeURIComponent(elHtml));
    link.click();
}

