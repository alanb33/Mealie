function try_load_food_db()
{
    console.log("Hello, world");
    if (food_db_json)
    {
        console.log("Food db loaded!");
        console.log(food_db_json)

        let food_list = document.querySelector("#food-db-item-list");
        for (let i = 0; i < food_db_json.length; i++)
        {
            if (food_db_json[i] != null)
            {
                let food_item = document.createElement("li");
                food_item.onmouseover = () => {
                    food_item.style.color = "red";
                }
                food_item.onmouseleave = () => {
                    food_item.style.color = "black";
                }
                food_item.onclick = () => {
    
                    // Remove the details if they already exist
                    let details = document.querySelector("#food-db-" + food_db_json[i].pk.toString() + "-details");
                    if (details)
                    {
                        details.remove();
                    }
                    else
                    {
                        // Show them!
                        let food_details = document.createElement("ul");
                        food_details.style.color="black";
                        food_details.id = "food-db-" + food_db_json[i].pk.toString() + "-details"; 
                        food_item.append(food_details);
                        let servings_line = document.createElement("li");
                        servings_line.innerHTML = "Serving size: " + food_db_json[i].fields.serving_size;
                        food_details.append(servings_line);
                        let calorie_line = document.createElement("li");
                        calorie_line.innerHTML = "Calories: " + food_db_json[i].fields.calories;
                        food_details.append(calorie_line);
                        let potassium_dv = document.createElement("li");
                        potassium_dv.innerHTML = "Potassium (%DV): " + food_db_json[i].fields.potassium_dv;
                        food_details.append(potassium_dv);
                        let calcium_dv = document.createElement("li");
                        calcium_dv.innerHTML = "Calcium (%DV): " + food_db_json[i].fields.calcium_dv;
                        food_details.append(calcium_dv);
                        let iron_dv = document.createElement("li");
                        iron_dv.innerHTML = "Iron (%DV): " + food_db_json[i].fields.iron_dv;
                        food_details.append(iron_dv);
                    }
                }
                food_item.innerHTML = food_db_json[i].fields.name;
                food_list.appendChild(food_item);    
            }
        }
    }
    else
    {
        console.log("Food db not loaded!");
    }
}

document.addEventListener("DOMContentLoaded", function()
{
    try_load_food_db();
});