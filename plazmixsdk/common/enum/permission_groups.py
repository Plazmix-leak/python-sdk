from plazmixsdk.common.enum.hierarchy import HierarchyEnum, HierarchyElement


# todo: Переписать
class PermissionGroup(HierarchyEnum):
    DEFAULT = HierarchyElement(0, "DEFAULT", "Игрок", html_color="gray")

    STAR = HierarchyElement(1, "STAR", "Star", html_color="#FFAA00")
    COSMO = HierarchyElement(2, "COSMO", "Cosmo", html_color="#76ff7a")
    GALAXY = HierarchyElement(3, "GALAXY", "Galaxy", html_color="#77dde7")
    UNIVERSE = HierarchyElement(4, "UNIVERSE", "UNIVERSE", html_color="#FF55FF")
    LUXURY = HierarchyElement(5, "LUXURY", "LUXURY", html_color="#FF5555")

    YOUTUBE = HierarchyElement(6, "YOUTUBE", "YouTube", html_color="#FFAA00")
    YOUTUBE_PLUS = HierarchyElement(7, "YOUTUBE_PLUS", "YouTube+", html_color="#FFAA00")

    TESTER = HierarchyElement(8, "TESTER", "QA", html_color="#AAAAAA")

    ART = HierarchyElement(9, "ART", "Дизайнер", html_color="#AA00AA")
    BUILDER = HierarchyElement(10, "BUILDER", "Строитель", html_color="#00AA00")
    BUILDER_PLUS = HierarchyElement(11, "BUILDER_PLUS", "Ст. Строитель", html_color="#00AA00")
    JUNIOR = HierarchyElement(12, "JUNIOR", "Мл. Модератор", html_color="#5555FF")
    MODERATOR = HierarchyElement(13, "MODERATOR", "Модератор", html_color="#5555FF")
    MODERATOR_PLUS = HierarchyElement(14, "MODERATOR_PLUS", "Ст. Модератор", html_color="#5555FF")

    ASSISTANT = HierarchyElement(15, "ASSISTANT", "Помощник", html_color="#AAAAAA")
    DEVELOPER = HierarchyElement(16, "DEVELOPER", "Разработчик", html_color="#00AAAA")
    ADMINISTRATOR = HierarchyElement(17, "ADMINISTRATOR", "Администратор", html_color="#FF5555")
    OWN = HierarchyElement(18, "OWNER", "Владелец", html_color="#AA0000")


DONATE_GROUPS = [PermissionGroup.STAR, PermissionGroup.COSMO, PermissionGroup.GALAXY,
                 PermissionGroup.UNIVERSE, PermissionGroup.LUXURY]

MODERATION_GROUPS = [PermissionGroup.MODERATOR_PLUS, PermissionGroup.MODERATOR,
                     PermissionGroup.JUNIOR]

STAFF_GROUPS = [PermissionGroup.OWN, PermissionGroup.ADMINISTRATOR, PermissionGroup.DEVELOPER,
                PermissionGroup.ASSISTANT, PermissionGroup.BUILDER_PLUS,
                PermissionGroup.BUILDER, PermissionGroup.ART]
STAFF_GROUPS.extend(MODERATION_GROUPS)
