## <class 'content.admin.ChallengesAdmin'>: (admin.E020) The value of 'filter_horizontal[0]' must be a many-to-many field.

fix -> The error <class 'content.admin.ChallengesAdmin'>: (admin.E020) The value of 'filter_horizontal[0]' must be a many-to-many field means you're trying to use a special widget for a field that isn't a many-to-many relationship.

In your Challenges model, the tags field is defined as a models.JSONField, which Django uses to handle PostgreSQL's text[] array type. The filter_horizontal widget, however, is exclusively for models.ManyToManyField. It provides a user interface for selecting multiple related objects, which doesn't apply to a simple array of text.

To fix this, you simply need to remove the filter_horizontal option from the ChallengesAdmin class.

I have removed the filter_horizontal = ('tags',) line from your content/admin.py file.

Once you've saved this change, please try running the server again. It should clear this specific error, and then we can address the next one.

---

## <class 'content.admin.ResourceMetaAdmin'>: (admin.E020) The value of 'filter_horizontal[0]' must be a many-to-many field.

fix -> removed the filter_horizontal

## <class 'content.admin.ResourceMetaAdmin'>: (admin.E020) The value of 'filter_horizontal[1]' must be a many-to-many field.

fix -> removed the filter_horizontal

## <class 'users.admin.NewsletterSubscriptionsAdmin'>: (admin.E002) The value of 'raw_id_fields[0]' refers to 'user_id', which is not a field of 'users.NewsletterSubscriptions'.

fix -> replaced user_id references to user

## users.admin.UserProfilesAdmin error

<class 'users.admin.UserProfilesAdmin'>: (admin.E035) The value of 'readonly_fields[0]' refers to 'other_details', which is not a callable, an attribute of 'UserProfilesAdmin', or an attribute of 'users.UserProfiles'.

<class 'users.admin.UserProfilesAdmin'>: (admin.E035) The value of 'readonly_fields[1]' refers to 'source_details', which is not a callable, an attribute of 'UserProfilesAdmin', or an attribute of 'users.UserProfiles'.

<class 'users.admin.UserProfilesAdmin'>: (admin.E035) The value of 'readonly_fields[2]' refers to 'communications', which is not a callable, an attribute of 'UserProfilesAdmin', or an attribute of 'users.UserProfiles'.

## **fix** -> removed other_details, source_details, and communications from readonly_fields of UserProfilesAdmin

users.Leads.program: (fields.E300) Field defines a relation with model 'program.Programs', which is either not installed, or is abstract.

users.Leads.program: (fields.E307) The field users.Leads.program was declared with a lazy reference to 'program.programs', but app 'program' doesn't provide model 'programs'.

users.UserEnrollments.program: (fields.E300) Field defines a relation with model 'program.Programs', which is either not installed, or is abstract.

users.UserEnrollments.program: (fields.E307) The field users.UserEnrollments.program was declared with a lazy reference to 'program.programs', but app 'program' doesn't provide model 'programs'.

users.UserMemberships.offering: (fields.E300) Field defines a relation with model 'content.Offerings', which is either not installed, or is abstract.

users.UserMemberships.offering: (fields.E307) The field users.UserMemberships.offering was declared with a lazy reference to 'content.offerings', but app 'content' doesn't provide model 'offerings'.

users.UserMemberships.transaction: (fields.E300) Field defines a relation with model 'user_transactions', which is either not installed, or is abstract.

users.UserMemberships.transaction: (fields.E307) The field users.UserMemberships.transaction was declared with a lazy reference to 'users.user_transactions', but app 'users' doesn't provide model 'user_transactions'.
