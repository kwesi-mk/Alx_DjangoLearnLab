from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app import Article

def setup_groups():
    """Create groups and assign permissions"""

    content_type = ContentType.objects.get_for_model(Article)

    # Define permissions
    view_permission = Permission.objects.get(codename="can_view", content_type=content_type)
    create_permission = Permission.objects.get(codename="can_create", content_type=content_type)
    edit_permission = Permission.objects.get(codename="can_edit", content_type=content_type)
    delete_permission = Permission.objects.get(codename="can_delete", content_type=content_type)

    #create groups 
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    editors, _ = Group.objects.get_or_create(name="Editors")
    admins, _ = Group.objects.get_or_create(name="Admins")

    # Assign permissions
    viewers.permissions.set([view_permissions])
    editors.permissions.set([view_permission, create_permission, edit_permission])
    admins.permissions.set([view_permission, create_permission, edit_permission, delete_permission])

    print("Groups and permissions set up successfully!")

# Call the function if running as a script
if __name__ == "__main__":
    setup_groups()