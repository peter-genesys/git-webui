ko.options.deferUpdates = true; //for performance - wait until values stabl before updating display 

// Class to represent a row in the seat reservations grid
function SeatReservation(name, initialMeal) {
    var self = this;
    self.name = name;
    self.meal = ko.observable(initialMeal);
}

// Overall viewmodel for this screen, along with initial state
function ReservationsViewModel() {
    var self = this;

    // Non-editable catalog data - would come from the server
    self.availableMeals = [
        { mealName: "Standard (sandwich)", price: 0 },
        { mealName: "Premium (lobster)", price: 34.95 },
        { mealName: "Ultimate (whole zebra)", price: 290 }
    ];    

    // Editable data
    self.seats = ko.observableArray([
        new SeatReservation("Steve", self.availableMeals[0]),
        new SeatReservation("Bert", self.availableMeals[0])
    ]);
}

//ko.applyBindings(new ReservationsViewModel());


//REPO_LIST
// Class to represent a repo
function Repo(name, path, branch) {
    var self = this;
    self.name = name;
    self.path = path;
    self.branch = branch;
}

// Overall viewmodel for this screen, along with initial state
function ReposViewModel() {
    var self = this;
 
    // Editable data
    self.repos = ko.observableArray([
        new Repo("Repo1", "Repo1path", "master")
       ,new Repo("Repo2", "Repo2path", "master")
       ,new Repo("Repo3", "Repo3path", "master")
    ]);
}

ko.applyBindings(new ReposViewModel());

