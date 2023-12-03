># [`open`.`source`.`threads`](https://imvickykumar999.github.io/open.source.threads/)
>
>     Daily Automated News Posts
>
> - `Google Apps Script` : [`Daily Function Calls`](https://script.google.com/u/0/home/projects/1UijQ7ly5WSLKrMLLgFDhYti71GWC7onL2jbdLwW6QsbvD8MCvRhjrfMv/edit)
>
>![image](https://github.com/imvickykumar999/open.source.threads/assets/50515418/e75859e9-44e0-495e-874e-f57276333852)
>
>![image](https://github.com/imvickykumar999/open.source.threads/assets/50515418/711c7a4d-95f3-4b6f-9c81-e7688618a799)
>
>![image](https://github.com/imvickykumar999/open.source.threads/assets/50515418/c375b87d-171b-44b7-8260-2057cbdd49db)

<br>

**Mastodon** *is* **a** ***decentralized*** *open source* **social media platform.**

    MASTODON Repo:
        https://github.com/mastodon/mastodon
    
    Application:
        https://mastodon.social/settings/applications/4958998

<br>

>## `Preferring Mastodon` ***over*** `Twitter or Threads`
>
>![image](https://github.com/imvickykumar999/open.source.threads/assets/50515418/ebee84ad-b85c-424c-a982-a8bb90df0712)

<br>

## `Threads` *v/s* `Mastodon`

    Threads is an app from Instagram that supports the ActivityPub protocol. 

Mastodon is a Twitter rival that also uses the ActivityPub protocol. 
    
    Threads is a way to read news and blogs. 
    It doesn't have hashtags. 
    
    Mastodon has an easy-to-use interface. 
    It has 1.8 million monthly active users and 2.34 million registered users. 
    
Threads and Mastodon are expected to be interoperable in the future. 
    
    This means that users will be able to follow each other and exchange messages. 
    
However, the operator of the Mastodon server will decide whether to allow communication with Threads. 

<br>

    Threads has some disadvantages, including: 
    
- Debugging and maintenance: Code becomes difficult to debug and maintain with more threads.
- System load: Thread creation puts a load on the system in terms of memory and CPU resources.
- Exception handling: Any unhandled exceptions can result in the program crashing.

<br>

What Is a Mastodon Instance? 
-----------

An instance is just another name for a server. Each server is running a version of the Mastodon software—an instance of that software.

<br>

    In Mastodon, an instance is a server that runs a version of the Mastodon software. 
    Instances are also called servers. 

Mastodon is a decentralized, open-source social media platform. Anyone can use Mastodon code to create a server for free. 

    Mastodon instances are individual communities, each with its own rules and culture. 
    These communities can be run by individuals, groups, or organizations. 
    
    They each have their own set of rules regarding how users can sign up, 
    as well as their own moderation policies. 

<br>

Mastodon.social is considered the flagship instance and has more than 41,700 users. 

    Some other instances include: 

- [c.im](https://c.im/home)
- [Social.wxcafe.net](https://social.wxcafe.net/about)
- [Octodon.social](https://octodon.social/about)
- ...
- [More Servers](https://joinmastodon.org/servers)
  
<br>

Why do I need a Mastodon application?
------------

All third-party integration with Mastodon occurs via a Mastodon application (an application defined at your Mastodon instance), and every application is owned by one and only one Mastodon profile. You could either develop and code your own service to operate your application, or you could use an existing service to act as your agent.

The SocialOomph service is the agent that acts as the operator of your Mastodon application.

This arrangement means you own the Mastodon application that posts to your Mastodon properties, and you use SocialOomph as the software engine to do that posting for you.

    It holds the following benefits:

- The Mastodon application belongs to you and only you can use it to publish posts to Mastodon.
- If any Mastodon application (other than your own) that also uses SocialOomph as an agent is restricted, deactivated, or deleted, your Mastodon application and your past Mastodon posts are not affected. In other words, you are insulated from undesireable posting behavior by other users and from erroneous account deactivations by Mastodon.
- Your Mastodon application's reputation (that the Mastodon instance administrator uses to impose restrictions and deactivations) relies solely on your posting behavior and is not affected by any undesirable posting behavior of anyone else.
- For the Mastodon instance administrator the benefit is that your Mastodon application operates within their rules and application management environment. In other words, they can enforce their policies and rules on your application with no impediment. Undesireable posting behavior can be identified and shut down much faster because it's not cloaked by the posting behavior of thousands of other users.
- For SocialOomph the benefit is that erroneous deactivation of personal profiles, deactivation of or restrictions imposed on a Mastodon application, and undesireable posting behavior by one user does not affect our entire user base.

--------------------

How do I create a Mastodon application?
-----------------

    To create a Mastodon application, please follow the steps below:

- In SocialOomph, use Social Networks, Network Apps, Add New Network App, Add Mastodon App in the menu.
- Open a new browser tab and login in to your account at your Mastodon instance.
- Click the gear icon (Preferences) icon to access your Mastodon preferences.
- Click Development in the left menu.
- Click the New Application button.
- Enter an Application Name of your choice.
- Enter https://www.socialoomph.com/mastodon/callback/ in the Redirect URI field (overwrite anything that is already in the field).
- Uncheck all the Scopes check boxes, and then check only the following check boxes: read:accounts, read:statuses, write: statuses, write: media.
- Click the Submit button.
- Click the hyperlinked name of your application.
- Copy the Client key and paste it into the SocialOomph Add Mastodon App form (Social Networks, Network Apps, Add New Network App, Add Mastodon App).
- Copy the Client secret and paste it into the SocialOomph Add Mastodon App form.
- Fill out the rest of the Add Mastodon App form and click the Save button.
