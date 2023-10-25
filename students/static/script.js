const editControls = document.querySelector(".input-toolbar-icons");

// autocomplete.js
const searchInput = document.getElementById("search-input");
const suggestionsList = document.getElementById("suggestions");
const resultsContainer = document.getElementById("results");

searchInput.addEventListener("input", function () {
    const query = this.value;
    if (query.trim() !== "") {
        fetch(`/search/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                suggestionsList.innerHTML = "";
                if (data.results.length > 0) {
                    data.results.forEach(result => {
                        const listItem = document.createElement("li");
                        listItem.textContent = result.threads;
                        listItem.style.color = "white";
                        listItem.style.marginLeft = "24px";
                        listItem.addEventListener("click", function () {
                            searchInput.value = result.threads;
                            suggestionsList.innerHTML = "";
                        });
                        suggestionsList.appendChild(listItem);
                    });
                    suggestionsList.style.display = "block";
                } else {
                    suggestionsList.style.display = "none";
                }
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    } else {
        suggestionsList.innerHTML = "";
        suggestionsList.style.display = "none";
    }
});

// Hide the results when clicking outside the autocomplete box
document.addEventListener("click", function (event) {
    if (event.target !== searchInput && event.target !== suggestionsList) {
        suggestionsList.innerHTML = "";
        suggestionsList.style.display = "none";
    }
});

editControls.addEventListener("click", function (event) {
  const command =
    event.target !== undefined &&
    event.target.getAttribute("data-command") !== null
      ? event.target.getAttribute("data-command")
      : null;
  if (command === null) return;
  console.log("Selected command: " + command);

  if (document.getSelection().toString().length === 0) {
    alert("Please select some text before editing the content.");
    return;
  }

  let range = window.getSelection().getRangeAt(0);
  const oldConent = document.createTextNode(range.toString());
  const newElement = document.createElement(command);
  newElement.append(oldConent);
  range.deleteContents();
  range.insertNode(newElement);
});

const closeSideBar = document.getElementById("close");
const sideBarWrapper = document.getElementById("sidebar-wrapper");
const sideBar = document.getElementById("user-sidebar");
const user = document.getElementById("user");

const info = document.getElementById("info");
const rightSidebarWrapper = document.getElementById("right-sidebar-wrapper");
const channelRightSidebar = document.getElementById("channel-right-sidebar");
const closeRightSidebar = document.getElementById("close-right-sidebar");

// sidebar
if (user) {
  user.addEventListener("click", () => {
    if (sideBarWrapper) {
      sideBarWrapper.classList.add("sidebar-wrapper-display");
    }
    if (sideBar) {
      sideBar.classList.add("user-sidebar-display");
    }
  });
}
if (closeSideBar) {
  closeSideBar.addEventListener("click", () => {
    sideBar.classList.remove("sidebar-display");
    sideBarWrapper.classList.remove("sidebar-wrapper-display");
  });
}

// Right sidebar displaying channel info

const enableInfoButton = (breaker) => {
  if (breaker.matches) {
    info.disabled = false;
    info.classList.remove("disabled");
  } else {
    info.disabled = true;
    info.classList.add("disabled");
  }
};

if (matchMedia) {
  const sidebarBreak = window.matchMedia("(max-width: 1250px)");
  sidebarBreak.addEventListener("change", enableInfoButton);
  enableInfoButton(sidebarBreak);
}

if (info) {
  info.addEventListener("click", () => {
    if (rightSidebarWrapper) {
      rightSidebarWrapper.classList.add("sidebar-wrapper-display");
    }
    if (channelRightSidebar) {
      channelRightSidebar.classList.add("channel-sidebar-display");
    }
  });
}

if (closeRightSidebar) {
  closeRightSidebar.addEventListener("click", () => {
    channelRightSidebar.classList.remove("channel-sidebar-display");
    rightSidebarWrapper.classList.remove("sidebar-wrapper-display");
  });
}

// click anywhere in the browser to close modals
window.onclick = (e) => {
  if (e.target == sideBarWrapper) {
    sideBar.classList.remove("sidebar-display");
    sideBarWrapper.classList.remove("sidebar-wrapper-display");
  } else if (e.target == rightSidebarWrapper) {
    channelRightSidebar.classList.remove("channel-sidebar-display");
    rightSidebarWrapper.classList.remove("sidebar-wrapper-display");
  }
};
