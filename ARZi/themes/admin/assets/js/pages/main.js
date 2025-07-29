import ARZi from "../compat/ARZi";
import Alpine from "alpinejs";
import $ from "jquery";
import dayjs from "dayjs";
import advancedFormat from "dayjs/plugin/advancedFormat";
import nunjucks from "nunjucks";
import { Howl } from "howler";
import events from "../compat/events";
import times from "../compat/times";
import "../compat/json";
import styles from "../styles";
import { default as helpers } from "../compat/helpers";

dayjs.extend(advancedFormat);

ARZi.init(window.init);
window.ARZi = ARZi;
window.Alpine = Alpine;
window.helpers = helpers;
window.$ = $;
window.dayjs = dayjs;
window.nunjucks = nunjucks;
window.Howl = Howl;

$(() => {
  styles();
  times();
  events(ARZi.config.urlRoot);
});
