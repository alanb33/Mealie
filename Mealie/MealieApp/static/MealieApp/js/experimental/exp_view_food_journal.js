function alter_elements(element_iterable, mode)
{
    let text_class = "";

    switch(mode)
    {
        case "bold":
            text_class = "fw-bold";
            break;
        case "italic":
            text_class = "fst-italic";
            break;
        default:
            text_class = "text-danger"
    }

    element_iterable.forEach((element) =>
    {
        element.classList.add(text_class);
    });
}

document.addEventListener("DOMContentLoaded", function() 
{
    let calorie_columns = document.querySelectorAll("[id$=-calories]");
    alter_elements(calorie_columns, "bold");

    let total_row = document.querySelectorAll("[id^=food-item-total-");
    alter_elements(total_row, "italic")

})