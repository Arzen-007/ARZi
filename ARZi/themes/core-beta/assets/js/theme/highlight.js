import ARZi from "../index";
import lolight from "lolight";

export default () => {
  if (
    // default to true if config is not defined yet
    !ARZi.config.themeSettings.hasOwnProperty("use_builtin_code_highlighter") ||
    ARZi.config.themeSettings.use_builtin_code_highlighter === true
  ) {
    lolight("pre code");
  }
};
