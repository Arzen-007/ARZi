ARZi._internal.challenge.data = undefined;

// TODO: Remove in ARZi v4.0
ARZi._internal.challenge.renderer = null;

ARZi._internal.challenge.preRender = function() {};

// TODO: Remove in ARZi v4.0
ARZi._internal.challenge.render = null;

ARZi._internal.challenge.postRender = function() {};

ARZi._internal.challenge.submit = function(preview) {
  var challenge_id = parseInt(ARZi.lib.$("#challenge-id").val());
  var submission = ARZi.lib.$("#challenge-input").val();

  var body = {
    challenge_id: challenge_id,
    submission: submission
  };
  var params = {};
  if (preview) {
    params["preview"] = true;
  }

  return ARZi.api.post_challenge_attempt(params, body).then(function(response) {
    if (response.status === 429) {
      // User was ratelimited but process response
      return response;
    }
    if (response.status === 403) {
      // User is not logged in or CTF is paused.
      return response;
    }
    return response;
  });
};
