# States Lookup Server

Just a little python server to support a US states type ahead style lookup in a client

## Usage

/lookup/[pattern]

Where [pattern] is a case insensitive starts with match for a states name

## Example

```
curl https://secure-tor-31050.herokuapp.com/lookup/ne

returns

{
  "states": [
    {
      "abbrv": "NE",
      "name": "Nebraska"
    },
    {
      "abbrv": "NV",
      "name": "Nevada"
    },
    {
      "abbrv": "NH",
      "name": "New Hampshire"
    },
    {
      "abbrv": "NJ",
      "name": "New Jersey"
    },
    {
      "abbrv": "NM",
      "name": "New Mexico"
    },
    {
      "abbrv": "NY",
      "name": "New York"
    }
  ]
}
```
