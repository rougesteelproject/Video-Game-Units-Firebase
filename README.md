# Overview

This is an experiment in using Firestore as a data storage solution.
I wanted to learn a new way of tackling the same problem.
I already have dabbled in SQL, Neo4j, and saving objects to disk as JSON files.
Because Firebase is structured similarly to JSON or to a dictionary, I imagined it would be simple to slot it into my existing projects.

Because I was immediately excited about the applications of Firestor in my existing projects, I wrote the database controller from scratch, but added it to a video game i had already made.
This is a stripped-down version of that game,, featuring only unit creation, the database controller, and anything they require to function.
In this demo, the software displays a tkinter-based gui which allows the user to input a unit's stats. When the unit is saved, it is sent to the Firestore cloud database.
When a unit is saved, users are taken to a gui page where they may search for a unit based on the values for 'name' and 'modpack' inserted earlier.
Firestore *will not* create or return a unit document if the creator email of the unit does not match the user's actual email. This is authenticated by google sign-in.

The purpose of the game is to be a testbed for a consistent pricing scheme for units in play-by-post games. The purpose of this element (that is, using firestore) is to be a more secure and resource-efficient way for users to create these units, or 'packs' of units, escpecially when compared to storing the data on the client side as files.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

This project uses Google Firestore.
Firestore stores data in the form of 'Collections' and 'Documents'. Collections are like folders, and contain Documents, where each document represents an entity. Documents have properties called fields, structured similarly to a dictionary or a JSON file.
Because Firestore does not allow assigning collection names to variables in it's security rules, it is impossible to give each user their own collection of documents (or in this specific case, of units). Instead of being structurally grouped, units are logically grouped by 'modpack' and by the email of their author.

# Development Environment

The software was developed in VSCode. The tkinter UI was initially built using Pygubu

This software was built in Python, and the firestore segment uses the *firebase_admin* module. The surrounding game demo uses the following modules:

* *logging* for error reporting
* *tkinter* for ui

# Useful Websites

* [Several questions on Stack Overflow - 1](https://stackoverflow.com/a/49919906)
* [Several questions on Stack Overflow - 2](https://stackoverflow.com/a/52424441)
* [Several questions on Stack Overflow - 3](https://stackoverflow.com/a/25854625)
* [Google's Cloud Python samples on Github](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/firestore/cloud-client/snippets.py#L121)
* [Google's own firestore doccumentation - 1](https://firebase.google.com/docs/firestore/quickstart)
* [Google's own firestore doccumentation - 2](https://cloud.google.com/firestore/docs/security/rules-conditions)
* [Google's own firestore doccumentation - 3](https://cloud.google.com/architecture/authenticating-users-to-firestore-with-identity-platform-and-google-identities)
* [Medium.com](https://medium.com/@bobthomas295/client-side-authentication-with-python-firestore-and-firebase-352e484a2634)
* [Google's Firebase Documentation](https://firebase.google.com/docs/reference/rest/auth)

# Future Work

* Using the '_read_and()' function (that is, a query with multiple WHERE clauses) to fetch individual units is complicated and seems like unclean code. It was written with the intent to find multiple units at a time with a given string in their name, similar to SQL's "%like%" symbol. Firestore does not and cannot perform a search like that. The firebase search function in this software can only retrieve a single unit of a given name, making the search function case-sensitive and underwhelming.
* The '_and' function, in practice, applies multiple 'where' clauses to a given query. I attempted to apply recursion to the function to avoid repeating code. Firestore requires that the symbols (">", "<", ">=", "<=", "!=") only be used on the field within a given request, and error prevention for this requires a complicated checking of the clauses given to the '_read_and()' function. Because a unit's name is it's document_id, searching for names in '_read_and()' is redundant (see above), but removing that clause turns '_read_and()' into a glorified wrapper for '_read_where()' where the program currently is using it. (This is because '_read_and()' will only pass one 'where' clause to '_read_where()'.) This seems more modular, but less efficeint than calling '_read_where()' directly in those cases.
* I expect that because a unit's name is used for it's document ID, it's possible to accidentally overwrite a unit. This is acceptable durring this testing phase, but will be frustrating to future users if not fixed. The current security rules prevent users from overwriting a unit that they did not create. In the future, we will need some form of versioning or other modification to the document (unit) naming scheme.
* The main game, of course, is still a work in progress, with a long TODO list.
