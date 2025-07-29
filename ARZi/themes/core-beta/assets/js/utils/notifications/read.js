import Alpine from "alpinejs";
import ARZi from "../../index";

export default () => {
  ARZi._functions.events.eventCount = count => {
    Alpine.store("unread_count", count);
  };

  ARZi._functions.events.eventRead = eventId => {
    ARZi.events.counter.read.add(eventId);
    let count = ARZi.events.counter.unread.getAll().length;
    ARZi.events.controller.broadcast("counter", { count: count });
    Alpine.store("unread_count", count);
  };

  document.addEventListener("alpine:init", () => {
    ARZi._functions.events.eventCount(ARZi.events.counter.unread.getAll().length);
  });
};
