function build_accordion(food_names_list, table_headers_verbose, table_headers_nonverbose)
{

    // Build the topmost accordion div
    let accordion_head = document.querySelector("#food-db-accordion");

    if (accordion_head != null)
    {
        accordion_head.textContent = "";
        build_accordion_items(accordion_head, food_names_list, table_headers_verbose, table_headers_nonverbose);
    }
    else
    {
        console.log("Accordion head is null");
    }   
}

function build_accordion_items(accordion_head, food_names_list, table_headers_verbose, table_headers_nonverbose)
{
    // Let's get the list of all the food items.
    console.log("Building heads");

    let accordion_container = document.querySelector("#accordion-container");
    console.log(accordion_container == null);

    for (let i = 0; i < food_names_list.length; i++)
    {
        let accordion_item = document.createElement("div");
        accordion_item.id = "accordion-item-" + i;
        accordion_item.classList.add("accordion-item");
        accordion_head.appendChild(accordion_item);

        let accordion_header = document.createElement("h2");
        let ah_button = document.createElement("button");
        ah_button.classList.add("accordion-button");
        ah_button.type="button";
        ah_button.dataset.bsToggle = "collapse";
        ah_button.dataset.bsTarget = "#collapse-food-item-body-" + i;
        ah_button.innerHTML = food_names_list[i].fields.name;
        
        accordion_header.appendChild(ah_button);
        accordion_item.appendChild(accordion_header);

        let item_body_div = document.createElement("div");
        item_body_div.id = "collapse-food-item-body-" + i;
        item_body_div.classList.add("accordion-collapse", "collapse");
        item_body_div.dataset.bsParent = "#food-db-accordion";

        accordion_item.append(item_body_div);
        let item_body = document.createElement("div");
        item_body.classList.add("accordion-body");
        item_body_div.appendChild(item_body);

        let body_row = document.createElement("div");
        body_row.classList.add("row");
        item_body.appendChild(body_row);

        // Column name column

        let header_column = document.createElement("div");
        header_column.classList.add("col-2", "text-end");
        body_row.append(header_column);

        for(let y = 0; y < table_headers_verbose.length; y++)
        {
            let table_header_p = document.createElement("p");
            table_header_p.classList.add("mb-0");
            header_column.append(table_header_p);

            let table_header_span = document.createElement("span");
            table_header_span.classList.add("fw-bold");
            table_header_span.innerHTML = table_headers_verbose[y];
            table_header_p.append(table_header_span);
        }

        // Column data column

        let data_column = document.createElement("div");
        data_column.classList.add("col-1", "text-start");
        body_row.append(data_column);

        for(let y = 0; y < table_headers_verbose.length; y++)
        {
            let table_header_p = document.createElement("p");
            table_header_p.classList.add("mb-0");
            data_column.append(table_header_p);

            let table_header_span = document.createElement("span");
            table_header_span.innerHTML = food_names_list[i].fields[table_headers_nonverbose[y]];
            if (table_headers_nonverbose[y].includes("dv"))
            {
                table_header_span.innerHTML += "%";
            }
            table_header_p.append(table_header_span);
        }

        // TODO: The display is upside-down... bodies are collapsing ABOVE the parent rather than below.
        // The current replication has paused on line 31 of the mock-up.
    }
}
