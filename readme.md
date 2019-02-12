# Hackathon Point!
## Important to Note
* host: gameathon.herokuapp.com/  
* `Authorization` di header: `Token <token>`  
* Get token from login first  
* DONT FORGET THE SLASH (/) AT THE END OF EVERY URL  
* U can access admin dashboard at `<host>/admin`
  
## API tree
```
tree:
|___rest-auth/
|   |___login/
|   |       POST returns token:
|   |           * username => str (optional)
|   |           * email => str (optional)
|   |           * password => str (required)
|   |
|   |___logout/
|           POST (no params)
|
|___add-point/
|       POST, params:
|           * game_type => str (required)
|           * point => int (required)
|           * chat_id => int (required)
|           * salt => str (required)
|
|
|   (ini FYI aja, ga dipake mustinya)
|___api/
    |___players/
    |       GET
    |       POST
    |       PUT
    |       PATCH
    |___players/<chat-id>
    |       GET
    |___transactions/
    |       GET
    |       POST
    |       PUT
    |       PATCH
    |___transactions/<id>
            GET
```

## QR CODE, delimiter: `;` with elements:
1. `salt`
2. `chat_id_str` (18 digits)
3. `username` (WITHOUT @) (may be empty)
4. `first_name` (may be empty)
5. `last_name` (may be empty)