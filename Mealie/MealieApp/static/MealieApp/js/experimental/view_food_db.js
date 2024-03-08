function buildAccordion(djangoVars)
{

    // Build the topmost accordion div
    let accordionHead = getAccordionHead();

    if (accordionHead != null)
    {
        accordionHead.textContent = "";
        buildAccordionItems(djangoVars);
    }
    else
    {
        console.log("Accordion head is null");
    }   
}

function getAccordionHead()
{
    return document.querySelector("#food-db-accordion");
}

function buildAccordionItems(djangoVars)
{
    // Let's get the list of all the food items.

    let accordionHead = getAccordionHead()
    let accordionContainer = document.querySelector("#accordion-container");

    for (let i = 0; i < djangoVars.foodNamesList.length; i++)
    {

        let accordionItem = document.createElement("div");
        accordionItem.id = "accordion-item-" + i;
        accordionItem.classList.add("accordion-item");
        accordionHead.appendChild(accordionItem);

        let accordionHeader = document.createElement("h2");
        let ahButton = document.createElement("button");
        ahButton.classList.add("accordion-button", "collapsed");
        ahButton.type="button";
        ahButton.dataset.bsToggle = "collapse";
        ahButton.dataset.bsTarget = "#collapse-food-item-body-" + i;
        ahButton.innerHTML = djangoVars.foodNamesList[i].fields.name;
        
        accordionHeader.appendChild(ahButton);
        accordionItem.appendChild(accordionHeader);

        let itemBodyDiv = document.createElement("div");
        itemBodyDiv.id = "collapse-food-item-body-" + i;
        itemBodyDiv.classList.add("accordion-collapse", "collapse");
        itemBodyDiv.dataset.bsParent = "#food-db-accordion";

        accordionItem.append(itemBodyDiv);
        let itemBody = document.createElement("div");
        itemBody.classList.add("accordion-body");
        itemBodyDiv.appendChild(itemBody);

        let bodyRow = document.createElement("div");
        bodyRow.classList.add("row");
        itemBody.appendChild(bodyRow);

        // Column name column

        let headerColumn = document.createElement("div");
        headerColumn.classList.add("col-2", "text-end");
        bodyRow.append(headerColumn);

        for(let y = 0; y < djangoVars.tableHeaders.verbose.length; y++)
        {
            let tableHeaderP = document.createElement("p");
            tableHeaderP.classList.add("mb-0");
            headerColumn.append(tableHeaderP);

            let tableHeaderSpan = document.createElement("span");
            tableHeaderSpan.classList.add("fw-bold");
            tableHeaderSpan.innerHTML = djangoVars.tableHeaders.verbose[y];
            tableHeaderP.append(tableHeaderSpan);
        }

        // Column data column

        let dataColumn = document.createElement("div");
        dataColumn.classList.add("col-1", "text-start");
        bodyRow.append(dataColumn);

        for(let y = 0; y < djangoVars.tableHeaders.verbose.length; y++)
        {
            let tableHeaderP = document.createElement("p");
            tableHeaderP.classList.add("mb-0");
            dataColumn.append(tableHeaderP);

            let tableHeaderSpan = document.createElement("span");
            tableHeaderSpan.innerHTML = djangoVars.foodNamesList[i].fields[djangoVars.tableHeaders.nonverbose[y]];
            if (djangoVars.tableHeaders.nonverbose[y].includes("dv"))
            {
                tableHeaderSpan.innerHTML += "%";
            }
            tableHeaderP.append(tableHeaderSpan);

        }

        // Column for edit and delete buttons

        let buttonColumn = document.createElement("div");
        buttonColumn.classList.add("col-2");
        buttonColumn.id = "food-item-button-column-" + i;
        bodyRow.appendChild(buttonColumn);

        let editButton = document.createElement("button");
        editButton.id = "food-item-edit-button-" + i;
        editButton.dataset.parentId = i;
        editButton.innerHTML = "Edit";
        editButton.classList.add("me-2");
        buttonColumn.appendChild(editButton);

        let deleteButton = document.createElement("button");
        deleteButton.id = "food-item-delete-button-" + i;
        deleteButton.dataset.parentId = i;
        deleteButton.innerHTML = "Delete";
        deleteButton.classList.add("btn-danger");
        deleteButton.onclick = () => confirmDeleteButtonTransformation(deleteButton, djangoVars.buttonUrls.delete);
        buttonColumn.appendChild(deleteButton);

    }

}

function confirmDeleteButtonTransformation(button, buttonUrl)
{
    button.innerHTML = "Are you sure?";
    //button.onclick = () => doDeletion(button.dataset.parentId, buttonUrl);
    button.type = "submit";
    button.onclick = () => location.href = buttonUrl;
}

function doDeletion(foodItemID, buttonUrl)
{
    console.log("Deleting food with ID of " + foodItemID);
    console.log("Opening URL " + buttonUrl);
}
