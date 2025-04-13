from django.db import models
from django.conf import settings
from allapps.Reponsebug.models import BugResponse  # anciennement ReponseBug
from allapps.Comment.models import CommentResponse

class LikeBugResponse(models.Model):
    """Model definition for likes on bug responses."""

    # reponse_bug = models.ForeignKey(ReponseBug, on_delete=models.CASCADE, related_name="likes")
    bug_response = models.ForeignKey(BugResponse, on_delete=models.CASCADE, related_name="likes")

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # date_creation = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('bug_response', 'user')  # Prevents a user from liking the same response more than once
        verbose_name = "Like Bug Response"
        verbose_name_plural = "Likes Bug Responses"

    def __str__(self):
        return f"{self.user} liked {self.bug_response}"



class LikeComment(models.Model):
    """Model definition for likes on comments."""

    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes comment")
    comment = models.ForeignKey(CommentResponse, on_delete=models.CASCADE, related_name="comment_likes")

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # date_creation = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('comment', 'user')  # Prevents duplicate likes
        verbose_name = "Like Comment"
        verbose_name_plural = "Likes Comments"

    def __str__(self):
        return f"{self.user} liked {self.comment}"
