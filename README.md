# [`open`.`source`.`threads`](https://github.com/mastodon/mastodon)

    Application : https://mastodon.social/settings/applications/4958998
    
    Hosting : https://www.socialoomph.com/mastodonapp/add/

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
