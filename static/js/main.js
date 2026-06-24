async function loadCoffees() {
    try {
        const response = await fetch("/coffees");
        const coffees = await response.json();

        const coffeeList = document.getElementById("coffee-list");
        coffeeList.innerHTML = "";

        coffees.forEach(coffee => {
            coffeeList.innerHTML += `
                <div class="coffee-card">
                    <div>
                        <h3>${coffee.name}</h3>
                        <p>Votes: ${coffee.votes}</p>
                    </div>

                    <button onclick="voteCoffee('${coffee.name}')">
                        Vote
                    </button>
                </div>
            `;
        });

    } catch (error) {
        console.error("Error loading coffees:", error);
    }
}

async function voteCoffee(name) {
    try {
        await fetch("/vote", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name
            })
        });

        loadCoffees();

    } catch (error) {
        console.error("Voting error:", error);
    }
}

loadCoffees();