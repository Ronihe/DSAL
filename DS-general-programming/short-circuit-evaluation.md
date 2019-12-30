# short-circuit evaluation

Short-circuit evaluation is a strategy most programming languages (including JavaScript) use to avoid unnecessary work. For example, say we had a conditional like this:

```
if (itIsFriday && itIsRaining) {
  console.log('board games at my place!');
}
```

Let's say itIsFriday is false. Because JavaScript short-circuits evaluation, it wouldn't bother checking the value of itIsRaining—it knows that either way the condition is false and we won't print the invitation to board game night.

We can use this to our advantage. For example, say we have a check like this:

```
if (friends['Becky'].isFreeThisFriday()) {
  inviteToBoardGameNight(friends['Becky']);
}
```

What happens if 'Becky' isn't in our friends object? Since friends['Becky'] is undefined, when we try to call isFreeThisFriday() we'll get a TypeError.

Instead, we could first confirm that Becky and I are still on good terms:

```
if (friends.hasOwnProperty('Becky') && friends['Becky'].isFreeThisFriday()) {
inviteToBoardGameNight(friends['Becky']);
}
```

This way, if 'Becky' isn't in friends, JavaScript will ignore the rest of the conditional and avoid throwing the TypeError.
