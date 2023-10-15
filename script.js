// Prompt:

/**
Strictly answer the following questions in one word i.e. in words of options, if the answer does not matches with any options, choose the most close or probable one.
*/

function run() {
    let question = document.querySelectorAll("#questionTd span")
    let options = document.querySelectorAll(".opDivSelectionBox span")
    
    console.log(
        "Question:", question[1].innerText, "\n", "Options are:", "\n", options[1].innerText, "\n", options[3].innerText, "\n", options[5].innerText, "\n", options[7].innerText, "\n"
    )
}

