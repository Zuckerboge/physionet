from __future__ import unicode_literals
from django.db import models
from catalog.models import BaseProject, ProjectDatabase, ProjectToolkit
from users.models import User

# Physionetworks project
class Project(BaseProject):

    # There will only be owner and collaborators who can all edit content. No reviewers.
    # pnw projects will be purely for publishing, not lingering, not for protected projects.

    owner  = models.ForeignKey(User, related_name='project_owner', blank=True)
    
    collaborators = models.ManyToManyField(User, related_name='project_collaborator', blank=True)
    
    # 0, 1, 2 = database, toolkit, documentation
    projecttype = models.SmallIntegerField()
    # Storage allowance in MB
    storage = models.SmallIntegerField(default=1024)
    # The requested storage allowance in MB
    requestedstorage = models.SmallIntegerField(default=None)

    # Depending on the project type, there will be additional info
    databaseinfo = models.OneToOneField(ProjectDatabase, blank=True)
    toolkitinfo = models.OneToOneField(ProjectToolkit, blank=True)
    #guideinfo = models.OneToOneField(blank=True)