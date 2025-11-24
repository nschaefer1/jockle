

async function go(page) {
    const map = {
        inventory:   'html/inventory.html',
        characters:  'html/characters.html'
        // Add HTML here
    };

    const file = map[page];
    if (!file) {
        console.error('Route not found:', page);
        return;
    }

    try {
        const absolutePath = await window.pywebview.api.resolve_path(file);
        window.location.href = 'file:///' + absolutePath;
    } catch (e) {
        console.error('Navigation failed:', e);
    }
}

// Make buttons work
window.go = go;