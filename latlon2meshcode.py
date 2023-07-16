from math import floor


class GridCell:
    def __init__(self, meshCode, longitude, latitude):
        self.meshCode = meshCode
        self.longitude = longitude
        self.latitude = latitude


class CoordinateCells:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    @property
    def first(self):
        degreeY = 40.0 / 60
        y = floor(self.latitude / degreeY)

        east = floor(self.longitude)
        x = east - 100

        return GridCell(
            meshCode=x + 100 * y,
            longitude=east,
            latitude=y * degreeY,
        )

    @property
    def second(self):
        degreeY = 5.0 / 60
        y = floor((self.latitude - self.first.latitude) / degreeY)

        degreeX = 7.5 / 60
        x = floor((self.longitude - self.first.longitude) / degreeX)

        return GridCell(
            meshCode=self.first.meshCode * 100 + y * 10 + x,
            longitude=self.first.longitude + x * degreeX,
            latitude=self.first.latitude + y * degreeY,
        )

    @property
    def third(self):
        degreeY = 30.0 / 60 / 60
        y = floor((self.latitude - self.second.latitude) / degreeY)

        degreeX = 45.0 / 60 / 60
        x = floor((self.longitude - self.second.longitude) / degreeX)

        return GridCell(
            meshCode=self.second.meshCode * 100 + y * 10 + x,
            longitude=self.second.longitude + x * degreeX,
            latitude=self.second.latitude + y * degreeY,
        )

    @property
    def fourth(self):
        degreeY = 15.0 / 60 / 60
        y = floor((self.latitude - self.third.latitude) / degreeY)

        degreeX = 22.5 / 60 / 60
        x = floor((self.longitude - self.third.longitude) / degreeX)

        code = (x + 1) + y * 2

        return GridCell(
            meshCode=self.third.meshCode * 10 + code,
            longitude=self.third.longitude + x * degreeX,
            latitude=self.third.latitude + y * degreeY,
        )

    @property
    def fifth(self):
        degreeY = 7.5 / 60 / 60
        y = floor((self.latitude - self.fourth.latitude) / degreeY)

        degreeX = 11.25 / 60 / 60
        x = floor((self.longitude - self.fourth.longitude) / degreeX)

        code = (x + 1) + y * 2

        return GridCell(
            meshCode=self.fourth.meshCode * 10 + code,
            longitude=self.fourth.longitude + x * degreeX,
            latitude=self.fourth.latitude + y * degreeY,
        )


coordinate_cells = CoordinateCells(138.4545, 36.4545)
first_mesh_code = coordinate_cells.first.meshCode
second_mesh_code = coordinate_cells.second.meshCode
third_mesh_code = coordinate_cells.third.meshCode
fourth_mesh_code = coordinate_cells.fourth.meshCode
fifth_mesh_code = coordinate_cells.fifth.meshCode


print(
    first_mesh_code,  # 5435
    second_mesh_code,  # 543553
    third_mesh_code,  # 54355346
    fourth_mesh_code,  # 543553463
    fifth_mesh_code,  # 5435534632
)
