# Module 1.10 — Idempotency Fundamentals

## Capability
Prevent repeated deliveries/retries from creating repeated business effects.

## Mental model
An operation is idempotent when performing the **same intended operation more than once has the same effective result as performing it once**.

This does not mean the server literally does no work on the second request. It means the important externally visible effect is not duplicated.

## Example: webhook
Event `evt_901` means "invoice paid".

Unsafe consumer:
```text
receive event
add $100 to revenue table
send fulfillment
```
If event is delivered twice, effects happen twice.

Safer pattern:
```text
receive event evt_901
check processed_event_ids
if already processed: acknowledge and stop
otherwise perform transaction and record evt_901
```

## Idempotency keys
Some APIs let clients send a unique key with a creation request. Retrying with the same key lets the service recognize the same logical operation. Follow provider semantics exactly; expiry and scope vary.

## IDs are design tools
Useful deduplication keys can come from:
- provider event ID;
- stable business ID;
- explicit idempotency key;
- composite unique constraint.

Avoid using timestamps alone as identity.

## Exercise
A CRM webhook may deliver `contact.updated` three times. Your automation sends an onboarding email when status changes to `customer`. Design state/data needed to guarantee the email is sent once per transition.

## Mastery
You can identify where duplication can happen and define the identity used to suppress duplicate effects.
