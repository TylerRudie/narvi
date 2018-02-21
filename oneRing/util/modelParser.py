
def modelParser(model):
    return [
                (f.name)
                for f in model._meta.get_fields()
                if f.concrete and (
                    not f.is_relation
                    or f.one_to_one
                    or (f.many_to_one and f.related_model)
                )
            ]
