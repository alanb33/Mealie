function check_for_food(food_name)
{
    console.log("compositionend triggered with " + food_name);
    let submit_button = document.querySelector("#food-submit");
    let submit_button_div = document.querySelector("#submit-div");
    for (let i = 0; i < all_food_names.length; i++)
    {
        if (all_food_names[i] != null)
        {
            let stored_food_name = all_food_names[i].fields.name;
            console.log("Preparing to compare " + food_name.toLowerCase() + " and " + stored_food_name.toLowerCase());
            if (food_name.toLowerCase() === stored_food_name.toLowerCase())
            {
                console.log("Food item found!!");
                submit_button.disabled = true;
                let warn_msg = document.createElement("p");
                warn_msg.classList.add("text-danger");
                warn_msg.id = "submit-name-invalid";
                warn_msg.innerHTML = "The food item \"" + food_name + "\" already exists in the database.";
                submit_button_div.appendChild(warn_msg);
                break;
            }
            else
            {
                if (submit_button.disabled)
                {
                    submit_button.disabled = false;
                    let warn_msg = document.querySelector("#submit-name-invalid");
                    if (warn_msg != null)
                    {
                        submit_button_div.removeChild(warn_msg)
                    }
                }
            }
        }
    }
}

document.addEventListener("DOMContentLoaded", function()
{
    let food_name_field = document.querySelector("#food-name")
    food_name_field.addEventListener("change", (event) => check_for_food(food_name_field.value))
});