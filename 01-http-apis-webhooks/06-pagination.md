# Module 1.6 — Pagination

## Capability
Retrieve a collection that does not fit in one API response without silently processing only the first page or creating an infinite loop.

## Why pagination exists
Returning 500,000 records in one response is expensive and unreliable. APIs therefore return bounded chunks.

## Common patterns
- page number: `?page=3&limit=100`
- offset: `?offset=200&limit=100`
- cursor: response gives a token/URL for the next page
- `next` link: response directly provides the next URL

Cursor-based pagination is common when data can change while you iterate.

## Safe loop mental model
```text
request first page
while another page exists:
    process current records
    calculate/read next-page marker
    request next page
stop when the contract says there is no next page
```

## Failure modes
- process only page one;
- forget to update cursor;
- reuse an old cursor forever;
- assume `len(records) < limit` always means last page when docs say otherwise;
- retry page creation operations and duplicate side effects;
- lose progress halfway through a long pagination job.

## Exercise
An API returns:
```json
{
  "items": [...],
  "next_cursor": "abc123"
}
```
The final page returns `"next_cursor": null`.

Write pseudocode that collects all item IDs and terminates safely. Add a maximum-page guard for debugging.

## Transfer
If records are inserted while you paginate, why might offset pagination cause duplicates or skipped records? You do not need a formal proof—explain the mechanism.

## Mastery
You can implement the pagination scheme described by docs instead of assuming one universal pattern.
