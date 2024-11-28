function addRow() {
  // Form data
  document.getElementById("myTable").style.display = "table";

  const formData = {};
  formData.presenter = document.getElementById("presenter").value;
  formData.lastName = document.getElementById("lastName").value;
  formData.firstName = document.getElementById("firstName").value;
  formData.email = document.getElementById("email").value;
  formData.firstNameInit = document.getElementById("firstNameInit").value;
  formData.affiliation = document.getElementById("affiliation").value;
  formData.city = document.getElementById("city").value;
  formData.country = document.getElementById("country").value;
  const myForm = document.getElementById("myForm");
  const tableBody = document.getElementById("myTableBody");
  const newRow = tableBody.insertRow();
  let cell;

  // Presenter
  cell = newRow.insertCell();
  cell.appendChild(document.createTextNode(formData.presenter));

  // Last Name
  cell = newRow.insertCell();
  cell.appendChild(document.createTextNode(formData.lastName));

  // First Name
  cell = newRow.insertCell();
  cell.appendChild(document.createTextNode(formData.firstName));

  // Email
  cell = newRow.insertCell();
  cell.appendChild(document.createTextNode(formData.email));

  // First Name İnit
  cell = newRow.insertCell();
  cell.appendChild(document.createTextNode(formData.firstNameInit));

  // Affilition
  cell = newRow.insertCell();
  cell.appendChild(document.createTextNode(formData.affiliation));

  // City
  cell = newRow.insertCell();
  cell.appendChild(document.createTextNode(formData.city));

  // Country
  cell = newRow.insertCell();
  cell.appendChild(document.createTextNode(formData.country));

  // Action
  cell = newRow.insertCell();
  const removeButton = document.createElement("button");
  removeButton.className = "btn btn-danger";
  removeButton.innerHTML = "X";
  removeButton.onclick = function () {
    const rowCount = tableBody.rows.length;
    if (rowCount === 1) {
      tableBody.deleteRow(0);
      document.getElementById("myTable").style.display = "none";
    } else {
      tableBody.deleteRow(rowCount - 1);
    }
  };
  cell.appendChild(removeButton);
  myForm.reset();
}
