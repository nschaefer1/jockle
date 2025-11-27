
async function handleItemClick(inv_ck) {
    console.log('Clicked item: ', inv_ck);
}

async function init(api) {
    
    // SELECT A DUMMY CHARACTER
    // TODO remove this line once we have character section
    await api.set_session('sel_char_ck', 1) // SELECTING VEYRA

    // load the inventory in the UI
    let sel_char_ck = await api.get_session('sel_char_ck')
    let response = await api.getInventory(sel_char_ck)
    if (!response.success) {
        console.log('API Call Failed')
        // TODO add error message in the container if possible
        return
    }

    console.log('API call successful');
    let container = document.getElementById('inventory-area');
    response.data.forEach(item => {

        // Creating a div element to add
        const div = document.createElement('div');

        // Attributes of the div element
        div.className = 'card';
        div.onclick = () => handleItemClick(item.inv_ck);

        // Creating img element
        const img = document.createElement('img');
        img.src = `../assets/icons/${item.icon_path ?? "uncertainty.png"}`;
        img.className = 'card-icon';
        // Add img to container
        div.appendChild(img);

        // Creating the count variable at the bottomr ight
        const num = document.createElement('div');
        if (item.item_count >= 1000000) {
            num.textContent = (item.item_count/1000000).toFixed(1) + "M";
        } else if (item.item_count >= 1000) {
            num.textContent = (item.item_count/1000).toFixed(1) + "K";
        } else {
            num.textContent = item.item_count;
        }
        num.className = 'card-num';
        // Add the number to the div
        div.appendChild(num);

        // HOVER Events
        div.addEventListener('mouseenter', () => {
            tooltip.innerHTML = `
                <strong>${item.inv_name}</strong><br>
                <p>${item.inv_desc}</p>
            `;
            tooltip.style.visibility = "visible";
            tooltip.style.opacity = "1";
        });
        div.addEventListener('mousemove', (e) => {
            tooltip.style.left = (e.pageX + 12) + 'px';
            tooltip.style.top = (e.pageY + 12) + 'px';
        });
        div.addEventListener('mouseleave', () => {
            tooltip.style.visibility = "hidden";
            tooltip.style.opacity = "0";
        });

        // Add card to container
        container.appendChild(div);

    });

}

window.addEventListener('pywebviewready', () => {
    let api = window.pywebview.api; // alias the API
    init(api);
})