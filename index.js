// Switch content dynamically based on some interaction (if needed)
function showContent(section) {
    const content = document.querySelector('.content');

    if (section === 'overview') {
        content.innerHTML = `
            <h2>Overview</h2>
            <p>This section provides an overview of the OrthoAntavirus and its monitoring details.</p>
        `;
    } else if (section === 'why-monitor') {
        content.innerHTML = `
            <h2>Why Monitor OrthoAntavirus?</h2>
            <p>Monitoring helps prevent outbreaks and ensures health interventions.</p>
        `;
    } else if (section === 'geo-map') {
        content.innerHTML = `
            <h2>Geo Location Map</h2>
            <img src="map-placeholder.png" alt="Map" style="width:100%; max-width:600px;">
        `;
    }
}
