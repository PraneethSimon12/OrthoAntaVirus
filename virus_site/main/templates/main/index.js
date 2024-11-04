// Function to switch between tabs
function showTab(tabId) {
    // Hide all tab content
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.style.display = 'none');

    // Remove 'active' class from all buttons
    const buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(button => button.classList.remove('active'));

    // Show the selected tab content
    document.getElementById(tabId).style.display = 'block';

    // Add 'active' class to the clicked button
    event.target.classList.add('active');
}

// Show Overview by default on page load
document.getElementById('overview').style.display = 'block';

// Function to search protein based on input
function searchProtein() {
    const protein = document.getElementById('protein-input').value.trim().toLowerCase();

    if (protein === 'nucleocapsid protein') {
        alert('Searching for Nucleocapsid Protein details...');
        // Logic to show content or navigate can go here
    } else if (protein === 'glycoprotein') {
        alert('Searching for Glycoprotein details...');
        // Logic to show content or navigate can go here
    } else {
        alert('Please enter a valid protein name from the options.');
    }
}
