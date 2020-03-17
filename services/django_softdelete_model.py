from django.db import models
from django.db.models.query import QuerySet


# 自定义逻辑删除model类，Begin：
class SoftDeleteQuerySet(QuerySet):
    def delete(self):
        self.update(is_deleted=True)


class SoftDeleteManager(models.Manager):
    """
    仅返回未被删除的实例
    """
    _queryset_class = SoftDeleteQuerySet

    def get_queryset(self):
        """
        在这里处理一下QuerySet, 然后返回没被标记位is_deleted的QuerySet
        """
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints

        return self._queryset_class(**kwargs).filter(is_deleted=False)


class SoftDeleteModel(models.Model):
    """
    抽象类，添加is_deleted 字段
    """
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    objects = SoftDeleteManager()

    def delete(self, using=None, soft=True, *args, **kwargs):
        """
        这里需要真删除的话soft=False即可
        """
        if soft:
            self.is_deleted = True
            self.save(using=using)
        else:
            return super(SoftDeleteModel, self).delete(using=using, *args, **kwargs)

# 自定义逻辑删除model类，End。