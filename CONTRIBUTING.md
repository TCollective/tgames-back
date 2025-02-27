# Branch Name Conventions:
(If you don't follow conventions no matter how important your contribution is it won't get merged)

## For feature update or new game:

dev/{contributor-name}/{game-name}/{relevant-name-to-your-work}

## For fixing issues:
dev{<contributor-name}/{game-name}/{fix-issue-number}

## URL Conventios:
Update tgames/urls.py with your game-name.urls.py url patterns

## Just Contributing in HTML,CSS,JS updates:
Update the templates/{game-name}/{all-the-games.html}
Update the static/{game-name}/{all-the-css-js}
Update the media/{game-name}/{all-images-and-icons}

## API Endpoint:
update your game-name.urls.py with a path: 
+ api/v{your-api-version}/{request-end-points}

## so our structure will be:
+ main game(with template view):
  - /game-name/
+ features:
  - /game-name/features
+ APIs:
  - /game-name/api/v{number}/features
