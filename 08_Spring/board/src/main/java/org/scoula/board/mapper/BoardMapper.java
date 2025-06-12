package org.scoula.board.mapper;

import org.scoula.board.domain.BoardVO;

import java.util.List;

public interface BoardMapper {
//    @Select("SELECT * FROM tbl_board ORDER BY no DESC")
    public List<BoardVO> getList();

    public BoardVO getOne(Long no);

    public void create(BoardVO board);

    public int update(BoardVO board);

    public int delete(Long no);
}
