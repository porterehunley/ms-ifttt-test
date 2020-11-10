# Graph QL query strings - might be better if we used graphQL

channel = "channel {\n    id\n    module_name\n    normalized_module_name\n  }"
ingrediants= "ingredients {\n    id\n    name\n    normalized_name\n    example\n    value_type\n  }"
trigger_fields= "trigger_fields {\n    id\n    name\n    label\n    field_ui_type\n    field_type\n    required\n    normalized_field_type\n    shareable\n    hideable\n    can_have_default\n    helper_text\n  }"
sepperator="\n"
triggers= "triggers {
    module_name
    name
    description
    id
    normalized_module_name
}"
