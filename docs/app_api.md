# App APIs

## Fetch Show Information
**URL**: GET /api/fetch-show?show_id={number}

Response Body
```
{
  "name": "Better Call Saul",
  "start_year": 2015,
  "end_year": 2022,
  "rating": "9.0",
  "age_rating": "TV-MA"
}
```

## Add Show Information
**URL**: POST /api/add-show

Request Body
```
{
  "name": "Breaking Bad",
  "start_year": 2008,
  "end_year": 2013,
  "rating": 9.5,
  "age_rating": "TV-MA"
}
```

Response Body
```
Added show
```

## Update Show Information
**URL**: PATCH /api/update-show

Request Body
```
{
  "show_id": 1,
  "name": "Better Call Saul",
  "start_year": 2015,
  "end_year": 2022,
  "rating": 9.0,
  "age_rating": "TV-MA"
}
```

Response Body
```
Updated show
```

## Delete Show Information
**URL**: DELETE /api/delete-show?show_id={number}

Response Body
```
Deleted show
```
