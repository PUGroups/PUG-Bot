# Programmers Universal Group Discord BOT (PUG Bot)
![a1412e5c-2794-47a2-a435-6c947724d477_rw_1200](https://user-images.githubusercontent.com/71369943/116653457-de0c2280-a9a4-11eb-924c-4fabee2aea13.gif)

This is the Programmers Universal Group Discord bot repo.

  
  <br>

## Contribute
You can freely contribute to the developement of this bot. To do it, just [open a pull request](https://github.com/PUGroups/PUG-Bot/compare/pull...main).
If you are issuing any kind of problem feel free to [open a new issue](https://github.com/PUGroups/PUG-Bot/issues/new) or to contact us on Discord. 
 
 
 ## Commands
 A full list of commands is available by using the help command (`?help`). Here's a detailed description of each command. The words beetween the <> are the arguments ("options") of the command.
 
- ### Music
	- `?play <song query>` allows anyone who is in a voice channel to listen a song. `song query` can be either a YouTube URL or a query  ot search on YouTube (in this case the first result will be automatically selected).
	- `?volume <volume>` allows anyone who is listening to a song to set the bot's volume. `volume` must be a value between 0 and 200.
	- `?stop` makes the bot leave the voice channel where the author is in.

- ### Polls
	- `?poll <text to poll>` allows anyone to start a poll in the channel where the command is sent.

- ### Other commands
	- `?info <user mention>` allows anyone to get info about the pinged user like the join date and the number of roles.
	- `?invite` creates an instant permanent invite to the server.

 - ### Moderation 
	 - `?ban <user mention>` allows moderators with the ban members permission to ban anyone in the server. This command works only with roles under the bot one.
	 - `?kick <user mention>` allows moderators with the kick members permission to kick anyone in the server. This command works only with roles under the bot one.
	 - `?unban <user ID>`  allows moderators with the ban members permission to unban anyone in the server. This command works with any banned member.
	 - `?clean <number of messsages>` allows people with admin permission to clean as many messages as they want.
	 - `?cleanup` allows people with admin permission to purge the last 40 messages up.
	 - `?mute <member mention>` allows admins to mute members. A `Muted` role is needed to get this feature working.
	 - `?unmute <member mention>` allows admins to unmute a previously muted member.
	 - `?addword <word to add>` allows admins to add a word to the swear filter. That word will be interted into the database and it will be censore when an user says it. 
	 - `?rmword <word to remove>` allows admins to remove a previously added custom swear word.
	 - `?infractions <user mention>` allows anyone to see the number of the infractions of the pinged user. This command does not require any permission.
	 - `?clearall <user mention>` allows admins to clear all the infractions that an user has.

## Coming soon:
 - `?warn` command (probably next version)
 - `?tempmute` command (later)
 - `?tempban` command (later)
 - Automtically add contributors to the developers database

## Resources
 - <a href="CODE_OF_CONDUCT.md">Code of Conduct</a>
 - <a href="CONTRIBUTING.md">Contribution rules</a>
 - <a href="Privacy%20Policy.md">Privay Policy</a>
 - <a href="LICENSE">License</a>


