import $ from "jquery";
import events from "../compat/events";
import ARZi from "../../compat/ARZi";

$(() => {
  events(ARZi.config.urlRoot);
});
