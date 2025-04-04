document.getElementById('generateBtn').addEventListener('click', function() {
    // Retrieve form values
    const receiptNo = document.getElementById('receiptNo').value;
    // const date = document.getElementById('date').value;
    const telephone = document.getElementById('telephone').value;
    const amount = document.getElementById('amount_').value;
    const from = document.getElementById('from').value;
    const location = document.getElementById('location').value;
    const otherLocation = document.getElementById('otherLocation').value;
    const paymentFor = document.querySelectorAll('.paymentFor');
    myArray =[];
    

    for(let i=0; i<paymentFor.length; i++){
        myArray.push("\n"+paymentFor[i].value); 
    }
    // Update receipt preview
    document.getElementById('displayReceiptNo').innerText = receiptNo;
    document.getElementById('displayAmount').innerText = amount;
    document.getElementById('displayFrom').innerText = from;
    if(otherLocation !== "" && (location == "Others" || location == "")  ){
    document.getElementById('displayLocation').innerText = otherLocation;
    }
    else{
        document.getElementById('displayLocation').innerText = location;
    }
    document.getElementById('displayTelephone').innerText = telephone;
    
    document.getElementById('displayPaymentFor').innerText = myArray;
    // document.getElementById('displayReceivedBy').innerText = receivedBy;

    // Show receipt and print button
    document.getElementById('receiptPreview').style.display = '';
    document.getElementById('receiptForm').style.display = 'none';
    document.getElementById('button-grp').style.display = '';
});

document.getElementById('editBtn').addEventListener('click', function() {
    document.getElementById('receiptPreview').style.display = 'none';
    document.getElementById('receiptForm').style.display = '';
    document.getElementById('button-grp').style.display = 'none';
});

document.getElementById('printBtn').addEventListener('click', function() {
    cart = {};
    window.print();
});




function autoFillDate() {
    // Get today's date
    let today = new Date();

    // Format the date to YYYY-MM-DD (HTML date input format)
    let day = String(today.getDate()).padStart(2, '0');
    let month = String(today.getMonth() + 1).padStart(2, '0');  // January is 0
    let year = today.getFullYear();

    // Create the formatted date string
    let formattedDate = `${year}-${month}-${day}`;

    // Set the value of the date input field
    // document.getElementById("dateField").value = formattedDate;
    document.getElementById('displayDate').innerText = formattedDate;

}

// Automatically fill the date when the page loads
window.onload = autoFillDate;