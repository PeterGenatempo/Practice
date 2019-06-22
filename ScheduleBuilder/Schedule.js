function Schedule() {
    this.month;
    this.shifts = [];
    this.employees = [];
}

function Employee() {
    this.name;
    this.daysOff = [];
    this.workingDays = [];
}

function buildSchedule(newSchedule) {
    sort(newSchedule.employees);

    for(var i = 0; i < newSchedule.shifts.length; i++) {
        var cont = true;

        for(var j = 0; j < newSchedule.employees.length; j++) {
            if(!newSchedule.employees[j].daysOff.includes(newSchedule.shifts[i].substring(0,5)) && cont) {
                newSchedule.employees[j].workingDays.push(newSchedule.shifts[i]);
                cont = false;
            }
        }

        sort(newSchedule.employees);
    }

    createSchedule(newSchedule);
}

function sort(arr) {
    var n = arr.length;

    for (var i = 0; i < n - 1; i++) {
        var min_idx = i;
        for (var j = i + 1; j < n; j++) {
            if (arr[j].workingDays.length < arr[min_idx].workingDays.length) {
                min_idx = j;
            }
        }

        var temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

function downloadSchedule(text, fileType, fileName) {
  var blob = new Blob([text], { type: fileType });

  var a = document.createElement('a');
  a.download = fileName;
  a.href = URL.createObjectURL(blob);
  a.dataset.downloadurl = [fileType, a.download, a.href].join(':');
  a.style.display = "none";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  setTimeout(function() { URL.revokeObjectURL(a.href); }, 1500);
}

function createSchedule(newSchedule) {
    var textSchedule = "";
    textSchedule += "-----" + newSchedule.month + " Schedule-----\n\n";

    for(var i = 0; i < newSchedule.employees.length; i++) {
        textSchedule += newSchedule.employees[i].name + "\n";

        textSchedule += "Days requested off:\n";
        for(var j = 0; j < newSchedule.employees[i].daysOff.length; j++) {
            textSchedule += newSchedule.employees[i].daysOff[j] + "\n";
        }

        textSchedule += "Scheduled shifts:\n";
        for(var k = 0; k < newSchedule.employees[i].workingDays.length; k++) {
            textSchedule += newSchedule.employees[i].workingDays[k] + "\n";
        }

        textSchedule += "\n";
    }

    downloadSchedule(textSchedule, ".txt", "schedule");
}

function main() {
    var input = prompt("Would you like to create a new schedule? (y/n)", "y");

    if(input == "y") {
        var newSchedule = new Schedule();
        input = prompt("What month is this schedule for?", "January");
        newSchedule.month = input;
        input = prompt("Would you like to add a new employee? (y/n)", "y");

        while(input == "y") {
            input = prompt("Enter employee name: ");
            let newEmployee = new Employee();
            newEmployee.name = input;
            newSchedule.employees.push(newEmployee);

            input = prompt("Would you like to add days off? (y/n)", "y");

            while(input == "y") {
                input = prompt("Enter day off (ex. 09/31)");
                newEmployee.daysOff.push(input);

                input = prompt("Would you like to add another day off? (y/n)", "y");
            }

            input = prompt("Would you like to add another new employee? (y/n)", "y");
        }

        input = prompt("Would you like to enter shifts? (y/n)", "y");

        while(input == "y") {
            input = prompt("Enter shift (ex. 06/03 7:00am-12:00pm)");
            newSchedule.shifts.push(input);

            input = prompt("Would you like to add another shift? (y/n)", "y");
        }

        if(newSchedule.employees.length != 0 && newSchedule.shifts.length != 0) {
            buildSchedule(newSchedule);
        } else {
            document.getElementById("output").innerHTML = "A schedule could not be made due to lack of shifts or employees";
        }
    } else {
        document.getElementById("output").innerHTML = "Goodbye";
    }
}
