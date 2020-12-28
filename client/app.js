function getDependentsValue() {
  var uiDependents = document.getElementsByName("uiDependents");
  for (var i in uiDependents) {
    if (uiDependents[i].checked) {
      return uiDependents[i];
    }
  }
  return -1; // Invalid Value
}


function onClickedApplyLoan() {
  console.log("Apply Loan button clicked");
  let gender = document.getElementById("uiGender");
  let married = document.getElementById("uiMarried");
  let dependents = getDependentsValue();
  let education = document.getElementById("uiEducation");
  let self_employed = document.getElementById("uiSelfEmployed");
  let applicantincome = document.getElementById("uiAIncome");
  let coapplicantincome = document.getElementById("uiCIncome");
  let loanamount = document.getElementById("uiLAmount");
  let loan_amount_term = document.getElementById("uiLAmountT");
  let credit_history = document.getElementById("uiCreditHistory");
  let property_area = document.getElementById("uiPropertyArea");
  let approval = document.getElementById("uiApplyLoan");
  let url = "/get_loan_approval"; 
  

  $.post(
    url,
    {
    gender : gender.value,
    married : married.value,
    dependents : dependents.value,
    education : education.value,
    self_employed : self_employed.value,
    applicantincome : parseFloat(applicantincome.value),
    coapplicantincome : parseFloat(coapplicantincome.value),
    loanamount : parseFloat(loanamount.value),
    loan_amount_term : parseFloat(loan_amount_term.value),
    credit_history : credit_history.value,
    property_area : property_area.value,
    },
    (data, status) => {
        console.log(data.loan_approval);
        approval.innerHTML =
            `<h2>${data.loan_approval}</h2>`;
        console.log(status);
    }
);
}
  