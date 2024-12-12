from drf_spectacular.utils import extend_schema, extend_schema_view


def create_schema_view(model_name, plural_name, tag_name, input_serializer, output_serializer):
    """
    Generates a decorator for ViewSets using drf-spectacular.

    :param model_name: The name of the model, for example, "Vehicle".
    :param plural_name: The name of many objects, for example, "avtomobillar".
    :param tag_name: The name of the tag, for example, "vehicles".
    :param input_serializer: A serializer for write operations (create, update).
    :param output_serializer: A serializer for reading operations (list, retrieve).
    :return: Decorator for the ViewSet
    """

    return extend_schema_view(
        list=extend_schema(
            summary=f"Barcha {plural_name}ni olish",
            tags=[tag_name],
            responses=output_serializer(many=True),
        ),
        retrieve=extend_schema(
            summary=f"{model_name} tafsilotlarini olish",
            tags=[tag_name],
            responses=output_serializer,
        ),
        create=extend_schema(
            summary=f"Yangi {model_name} qo'shish",
            tags=[tag_name],
            request=input_serializer,
            responses=output_serializer,
        ),
        update=extend_schema(
            summary=f"{model_name} ma'lumotlarini yangilash",
            tags=[tag_name],
            request=input_serializer,
            responses=output_serializer,
        ),
        partial_update=extend_schema(
            summary=f"{model_name} ma'lumotlarini qisman yangilash",
            tags=[tag_name],
            request=input_serializer,
            responses=output_serializer,
        ),
        destroy=extend_schema(
            summary=f"{model_name}ni o'chirish",
            tags=[tag_name],
            responses={204: f"{model_name} muvaffaqiyatli o'chirildi"},
        ),
    )