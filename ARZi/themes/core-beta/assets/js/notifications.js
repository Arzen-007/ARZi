import Alpine from "alpinejs";
import ARZi from "./index";

window.ARZi = ARZi;
window.Alpine = Alpine;

// Get unread notifications from server
let lastId = ARZi.events.counter.read.getLast();
ARZi.fetch(`/api/v1/notifications?since_id=${lastId}`)
  .then(response => {
    return response.json();
  })
  .then(response => {
    // Get notifications from server and mark them as read
    let notifications = response.data;
    let read = ARZi.events.counter.read.getAll();
    notifications.forEach(n => {
      read.push(n.id);
    });
    ARZi.events.counter.read.setAll(read);

    // Mark all unread as read
    ARZi.events.counter.unread.readAll();

    // Broadcast our new count (which should be 0)
    let count = ARZi.events.counter.unread.getAll().length;
    ARZi.events.controller.broadcast("counter", {
      count: count,
    });
    Alpine.store("unread_count", count);
  });

Alpine.start();
